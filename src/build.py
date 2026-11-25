"""Builds ../index.html from template.html by inlining the PNG assets as data URIs."""
import base64, pathlib
here = pathlib.Path(__file__).parent
t = (here / "template.html").read_text(encoding="utf-8")
uri = lambda f: "data:image/png;base64," + base64.b64encode((here / "assets" / f).read_bytes()).decode()
t = t.replace("@@SCENE@@", uri("screen-scene.png")).replace("@@TEX@@", uri("button-texture.png"))
(here.parent / "index.html").write_text(t, encoding="utf-8")
print("index.html built")
