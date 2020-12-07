-- A table that maps bag colors onto a table of colors:quantity that can contain it.
-- Note that this is the reverse of the specification in the input file,
--  which declares a bag color and defines the colors of bags that may be
--  placed inside.
-- For example, we might have Bags["shiny gold"]["hearing aid beige"] == 3,
--  meaning that a hearing aid beige bag may contain 3 shiny gold bags.
Bags = {}
Externalbags = {}

-- Given a `bagname` and a valid `contents` string, populate `Bags` with the association.
-- A "contents string" is defined as anything that can validly follow "contains" on a
--  line in the input file, WITHOUT whitespace.
-- This function recursively takes advantage of the property that stripping away each
--  bag's complete description in the contents string can result in either a fixed
--  value (in this case, the empty string), or another valid contents string.
function RecordBagContents(bagname, contents)
  -- print(bagname, contents)
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
  
  -- 
  if Bags[color] == nil then
    Bags[color] = {}
  end
  
  Bags[color][bagname] = number
  
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

-- Returns how many bag colors can possibly hold an `enclosedbag` color bag.
--  This function depends on side effects, namely storing a running table of
--  how many times each bag has been visited in `Externalbags`, in order to
--  avoid double-counting.
function Howmanybagshold(enclosedbag)
  local count = 0

  -- Here's our base case: If `enclosedbag` isn't in the table, then
  --  nothing can hold it, so we return 0.
  if not Bags[enclosedbag] then
    return 0
  end

  for enclosingbag, ct in pairs(Bags[enclosedbag]) do
    -- NB: This is NOT tail recursive, so things could get ugly for very large
    --     input sizes.

    -- If we have not yet counted this enclosing bag, then add it to the table
    --  with a zero value, and increment our local count.
    if Externalbags[enclosingbag] == nil then
      Externalbags[enclosingbag] = 0
      -- Increment the running size of the table.
      -- TODO: Is this needed? I should read the lua docs more for this.
      table.setn(Externalbags, table.getn(Externalbags)+1)
      -- Increment our local count, which we'll be returning.
      count = count + 1
    end
    -- Increment the number of times that enclosingbag has been reached
    --  as a candidate for an outermost bag.
    Externalbags[enclosingbag] = Externalbags[enclosingbag] + 1
    -- Recurse. (Again, note: because this is called in a loop, possibly
    --  even multiple times prior to recursing, plus being part of an
    --  arithmetic expression, this is NOT tail recursion.
    count = count + Howmanybagshold(enclosingbag)
  end
  return count
end

-- Produce a string representation of a (possibly nested) table.
-- From Matt on Stack Overflow at <https://stackoverflow.com/a/27028488>
-- Note: this does NOT use tail recursion! So, for enormous tables, it
--  may result in a Stack Overflow (lol).
function dump(o)
  if type(o) == 'table' then
    local s = '{ '
    for k,v in pairs(o) do
      if type(k) ~= 'number' then k = '"'..k..'"' end
      s = s .. '['..k..'] = ' .. dump(v) .. ','
    end
    return s .. '} '
  else
    return tostring(o)
  end
end

-- And we're off to see the wizard.
Recordbags('input.txt')

print(Howmanybagshold("shiny gold"))
