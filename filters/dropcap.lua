function Span(span)
    if span.classes:includes("dropcap") then
      local text = pandoc.utils.stringify(span.content)
      return pandoc.RawInline("typst", "#dropcap(\"" .. text .. "\")")
    end
  end