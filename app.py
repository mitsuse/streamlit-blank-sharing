from __future__ import annotations

import streamlit as st


def main() -> None:
    from PIL.Image import new as new_image

    st.title("Blank Image")

    image = new_image('RGB', (128, 128), color='gray')

    st.image(image)

    st.header("Options")

    keys = (
        "browser.serverAddress",
        "browser.serverPort",
        "server.address",
        "server.port",
        "server.baseUrlPath",
    )

    for k in keys:
        st.text(f"{k}: {st.get_option(k)}")


main()
