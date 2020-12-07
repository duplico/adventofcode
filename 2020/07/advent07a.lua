local bags

function RecordBagContents(bagname, contents)
     print(bagname, contents)
     if contents == "" or contents == "no other bags." then
          -- Done, nothing to do.
          print("Nothing to do.")
          return
     end
     -- There's something to do.
     local number, color, remainder = string.match(contents, "(%d) (.-) bags?[,.]%s?(.*)")
     print(bagname, number, color, remainder)

     RecordBagContents(bagname, remainder)
end

function Recordbags()
     for line in io.lines('sample_input.txt') do
          local bagname, contents
          bagname, contents = string.match(line, "(.+) bags? contain (.+)")
          -- print(bagname, contents)
          RecordBagContents(bagname, contents)
     end
end

Recordbags()
