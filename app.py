import os
import streamlit as st

# Optional Gemini import. The app can also run in Demo/Template mode
# without an API key, which makes classroom demonstration easier.
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

st.set_page_config(
    page_title="E-Commerce Product Content Generator",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ E-Commerce Product Content Generator")
st.write(
    "Generate e-commerce-ready product titles, descriptions, bullet points, "
    "SEO keywords, and a short marketing tagline from basic product information."
)

with st.sidebar:
    st.header("Generation Settings")
    mode = st.radio(
        "Generation Mode",
        ["Demo / Template Mode", "Gemini AI Mode"],
        index=0
    )
    tone = st.selectbox(
        "Content Tone",
        ["Professional", "Friendly", "Premium", "Persuasive"]
    )
    description_length = st.selectbox(
        "Description Length",
        ["Short", "Medium", "Detailed"]
    )

st.subheader("1. Enter Product Information")

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product Name", "Wireless Bluetooth Headphones")
    category = st.text_input("Category", "Audio / Headphones")
    brand = st.text_input("Brand", "SoundMax")
    price = st.text_input("Price", "₹2,999")

with col2:
    features = st.text_area(
        "Key Features (one per line)",
        "Bluetooth 5.3\n40-hour battery life\nActive Noise Cancellation\n"
        "Fast USB-C charging\nComfortable over-ear design"
    )
    target_audience = st.text_input(
        "Target Audience",
        "Students, professionals and music lovers"
    )

def clean_features(raw_features):
    return [x.strip(" •-\t") for x in raw_features.splitlines() if x.strip()]

def template_generate(name, category, brand, price, features, audience, tone, length):
    feature_text = ", ".join(features[:5])
    bullets = "\n".join([f"• {f}" for f in features[:5]])

    if tone == "Premium":
        tagline = f"Elevate every listening moment with {name}."
    elif tone == "Friendly":
        tagline = f"Meet your new everyday audio companion: {name}."
    elif tone == "Persuasive":
        tagline = f"Upgrade your everyday sound with {name}."
    else:
        tagline = f"Reliable, immersive audio for everyday listening."

    if length == "Short":
        desc = (
            f"{name} is a {category.lower()} from {brand}, designed for "
            f"{audience.lower()}. It combines {feature_text.lower()} to deliver "
            f"a convenient and enjoyable listening experience."
        )
    elif length == "Detailed":
        desc = (
            f"{name} is a feature-rich {category.lower()} from {brand}, created "
            f"for {audience.lower()}. It brings together {feature_text.lower()} "
            f"for a balanced combination of convenience, comfort and performance. "
            f"The product is suitable for everyday use such as study, work, "
            f"travel and entertainment. At {price}, it is positioned as a practical "
            f"choice for customers looking for useful features in one device."
        )
    else:
        desc = (
            f"{name} is a {category.lower()} from {brand}, built for "
            f"{audience.lower()}. With {feature_text.lower()}, it offers a "
            f"comfortable and convenient experience for study, work, travel "
            f"and entertainment."
        )

    title = f"{brand} {name} – {features[0] if features else 'Feature-Rich Design'}"
    keywords = ", ".join([
        name.lower(), brand.lower(), category.lower(),
        "wireless headphones", "bluetooth headphones",
        "noise cancelling headphones", "headphones for students"
    ])

    return {
        "title": title,
        "description": desc,
        "bullets": bullets,
        "keywords": keywords,
        "tagline": tagline
    }

def gemini_generate(name, category, brand, price, features, audience, tone, length):
    if not GEMINI_AVAILABLE:
        raise RuntimeError("google-genai is not installed.")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to your environment and restart the app."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an e-commerce product content specialist.

Generate accurate marketing content using ONLY the product facts supplied below.
Do not invent specifications, certifications, discounts, warranty terms, ratings,
or performance claims that are not provided.

Product name: {name}
Category: {category}
Brand: {brand}
Price: {price}
Target audience: {audience}
Tone: {tone}
Description length: {length}
Known features:
{chr(10).join('- ' + f for f in features)}

Return exactly these sections:
TITLE:
DESCRIPTION:
BULLET POINTS:
SEO KEYWORDS:
TAGLINE:
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return {"raw": response.text}

features_list = clean_features(features)

if st.button("✨ Generate Product Content", type="primary", use_container_width=True):
    if not product_name.strip():
        st.error("Please enter a product name.")
    elif not features_list:
        st.error("Please enter at least one product feature.")
    else:
        with st.spinner("Generating product content..."):
            if mode == "Gemini AI Mode":
                try:
                    result = gemini_generate(
                        product_name, category, brand, price,
                        features_list, target_audience, tone, description_length
                    )
                    st.success("AI-generated content created successfully.")
                    st.subheader("Generated Content")
                    st.text_area("Output", result["raw"], height=420)
                except Exception as e:
                    st.warning(
                        f"Gemini AI mode could not be used: {e}\n\n"
                        "Showing Demo/Template output instead."
                    )
                    result = template_generate(
                        product_name, category, brand, price,
                        features_list, target_audience, tone, description_length
                    )
                    st.subheader("Generated Content")
                    st.markdown(f"**Product Title:** {result['title']}")
                    st.markdown(f"**Description:** {result['description']}")
                    st.markdown("**Key Selling Points:**")
                    st.markdown(result["bullets"])
                    st.markdown(f"**SEO Keywords:** {result['keywords']}")
                    st.markdown(f"**Tagline:** {result['tagline']}")
            else:
                result = template_generate(
                    product_name, category, brand, price,
                    features_list, target_audience, tone, description_length
                )
                st.success("Demo content generated successfully.")
                st.subheader("Generated Content")
                st.markdown(f"**Product Title:** {result['title']}")
                st.markdown(f"**Description:** {result['description']}")
                st.markdown("**Key Selling Points:**")
                st.markdown(result["bullets"])
                st.markdown(f"**SEO Keywords:** {result['keywords']}")
                st.markdown(f"**Tagline:** {result['tagline']}")

st.divider()
st.caption(
    "Academic prototype: always verify generated product content against the "
    "actual product specifications before publishing."
)
