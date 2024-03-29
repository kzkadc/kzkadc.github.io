import yaml


def main():
    with open("publications.yaml", "r", encoding="utf-8") as f:
        publications = yaml.safe_load(f)

    sections = []

    for section in publications:
        papers = []
        for paper in section["papers"][::-1]:
            authors = ", ".join(paper["authors"])
            title = paper['title']
            pub = paper['published_in']
            bib = f"- {authors}. \"**{title}**\" {pub}"

            # links = []
            # if url := paper.get("publication_url"):
            #     links.append(f"[[Paper]]({url})")
            # if url := paper.get("preprint_url"):
            #     links.append(f"[[Preprint]]({url})")
            # if len(links) >= 1:
            #     bib += f"  \n{' '.join(links)}"

            link_list = []
            for link in paper.get("links", []):
                text, url = next(iter(link.items()))
                link_list.append(f"[[{text}]]({url})")
            if len(link_list) >= 1:
                bib += f"  \n{' '.join(link_list)}"

            papers.append(bib)

        papers = "\n".join(papers)
        sections.append(f"### {section['section_name']}\n{papers}")

    sections = "\n\n".join(sections)
    with open("generated_publications.md", "w", encoding="utf-8") as f:
        f.write(sections)


if __name__ == "__main__":
    main()
