#set page(size: "6in 9in", margin: 1in)

#set font(font.family: "Georgia", font.size: 11pt)

#define dropcap(text) = text[weight: bold, size: 36pt, color: rgb(0.1,0.1,0.1)]

#define chapter_title(title) = (
  vbox(
    skip(1in),
    text(title, align: center, weight: bold, size: 24pt),
    skip(0.3in),
    rule(),
    skip(0.3in),
  )
)

#let header_text = "My Novel Title"

#set page-numbering(start: 1)

#set header(content: header_text + " - " + page.chapter)
#set footer(content: page.number)

#for chapter in book.chapters:
  chapter_title(chapter.title)
  #for paragraph in chapter.content:
    #if paragraph.starts_with("*") and paragraph.count("*") == 3:
      skip(0.2in)  # scene break
      centered("***")
      skip(0.2in)
    #else:
      if paragraph == chapter.content[0]:
        # — first paragraph, apply drop cap
        paragraph[0] = dropcap(paragraph[0])
      text(paragraph)
      skip(0.1in)
