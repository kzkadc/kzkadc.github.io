import yaml


def main():
    with open("publications.yaml", "r", encoding="utf-8") as f:
        publications = yaml.safe_load(f)

    sections = []

    for section in publications:
        papers = []
        for paper in section["papers"]:
            authors = ", ".join(paper["authors"])
            bib = f"- {authors}. \"**{paper['title']}**\" {paper['published_in']}"

            links = []
            if url := paper.get("publication_url"):
                links.append(f"[[Paper]]({url})")
            if url := paper.get("preprint_url"):
                links.append(f"[[Preprint]]({url})")
            if len(links) >= 1:
                bib += f"  \n{' '.join(links)}"

            papers.append(bib)

        papers = "\n".join(papers)
        sections.append(f"### {section['section_name']}\n{papers}")

    sections = "\n\n".join(sections)
    with open("generated_publications.md", "w", encoding="utf-8") as f:
        f.write(sections)


if __name__ == "__main__":
    main()
