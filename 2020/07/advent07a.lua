Bags = {}

-- Given a `bagname` and a valid `contents` string, populate `Bags` with the association.
-- A "contents string" is defined as anything that can validly follow "contains" on a
--  line in the input file, WITHOUT whitespace.
-- This function recursively takes advantage of the property that stripping away each
--  bag's complete description in the contents string can result in either a fixed
--  value (in this case, the empty string), or another valid contents string.
function RecordBagContents(bagname, contents)
     print(bagname, contents)
     -- This if statement gets us our base case.
     -- If the contents string is "no other bags", then this is a bag that
     --  is not allowed to contain any other bags. If the contents string
     --  is empty, it means that we have already consumed any and all possible
     --  contents of the bag.
     if contents == "" or contents == "no other bags." then
          -- Done, nothing to do.
          return
     end
     -- This is the general case: the contents string contains at least one
     --  bag that may be enclosed in a `bagname` bag. Identify, non-greedily
     --  (hence `(.-)`) the first bag's `number` and `color`, storing the
     --  remainder of 
     local number, color, remainder = string.match(contents, "(%d) (.-) bags?[,.]%s?(.*)")
     print(bagname, number, color, remainder)

     -- Recur.
     -- (Note: There's no syntactic sugar here for tail recursion,
     --  unlike in Clojure, because Lua natively supports tail-call
     --  optimization. So we just call the function.)
     RecordBagContents(bagname, remainder)
end

-- Given a `filename`, read every rule in the file and populate the `Bags` table.
function Recordbags(filename)
     -- Read the input file one line at a time. For each line...
     for line in io.lines(filename) do
          local bagname, contents
          -- Split the line into the name of the bag and a "contents string",
          --  which is the name we're giving any valid description of the
          --  possible contents of a bag that follows the word "contain",
          --  after stripping away the whitespace.
          bagname, contents = string.match(line, "(.+) bags? contain (.+)")

          -- Call RecordBagContents (which is basically Side Effects City, so
          --  much for our funtional party) to store these specifications in
          --  a global table called `Bags`.
          RecordBagContents(bagname, contents)
     end
end

-- And we're off to see the wizard.
Recordbags('sample_input.txt')
