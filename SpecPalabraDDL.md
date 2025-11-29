# Palabra DDL Language Specification

**Author:** [palabra](https://github.com/palabra)  
**License:** [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)  

---

## 1. Introduction

Palabra DDL is a **hierarchical, level-based, schema-free data definition language**.  
It is designed to represent tree-structured data in a **compact, human-readable, and machine-parseable format**.  

Key features:

- **Schema-free:** Users can define any keys at any depth.  
- **Hierarchical:** Structure is determined by numeric levels.  
- **Flexible:** Works for AI tech trees, personal profiles, configurations, or any nested data.  
- **Whitespace-safe:** Numeric levels replace indentation.  

---

## 2. Syntax

Each line has the format:
