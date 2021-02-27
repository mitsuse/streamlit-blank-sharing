from __future__ import annotations

import streamlit as st


def main() -> None:
    from PIL.Image import new as new_image

    st.title("Blank Image")

    image = new_image('RGB', (128, 128), color='gray')

    st.image(image)


main()
