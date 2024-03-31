import pypandoc


class Pandoc:
    @staticmethod
    def convert_text(source: str, to: str, frm: str) -> str:
        return pypandoc.convert_text(source, to, frm)
