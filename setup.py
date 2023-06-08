from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="asm-opcode-analyzer",
    version="1.0.0",
    author="Mustaqeem",
    author_email="mustaqeem.whyne@gmail.com",
    description="Python package for analyzing ASM opcodes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhammad-mustaqeem/ASM-Opcode-Analyzer",
    packages=["asm_opcode_analyzer"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
