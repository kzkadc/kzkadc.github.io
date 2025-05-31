import yaml


def main():
    with open("publications.yaml", "r", encoding="utf-8") as f:
        publications = yaml.safe_load(f)

    sections = []

    for section in publications:
        papers = []
        for paper in section["papers"]:
            authors = ", ".join(paper["authors"])
            title = paper["title"]
            pub = paper["published_in"]
            bib = f"- {authors}. **\"{title}\"** {pub}"

            link_list = []
            for link in paper.get("links", []):
                text, url = next(iter(link.items()))
                link_list.append(f"[[{text}]]({url})")
            if len(link_list) >= 1:
                bib += f"  \n{' '.join(link_list)}"

            if "abstract" in paper:
                bib += f" <details><small><i>{paper['abstract']}</i></small></details>"

            papers.append(bib)

        papers = "\n".join(papers)
        sections.append(f"### {section['section_name']}\n{papers}")

    sections = "\n\n".join(sections)
    with open("generated_publications.md", "w", encoding="utf-8") as f:
        f.write(sections)


if __name__ == "__main__":
    main()
