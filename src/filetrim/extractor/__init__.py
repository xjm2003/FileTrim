from filetrim.extractor.base import BaseExtractor, extract_content, get_extractor
from filetrim.extractor.docx_extractor import DocxExtractor
from filetrim.extractor.pdf_extractor import PdfExtractor
from filetrim.extractor.text_extractor import TextExtractor

__all__ = [
    "BaseExtractor",
    "DocxExtractor",
    "PdfExtractor",
    "TextExtractor",
    "extract_content",
    "get_extractor",
]
