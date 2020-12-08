-- A table that maps bag colors onto a table of colors:quantity that it can contain.
-- Note that this directly corresponds to the order of the specification of the
--  input file, which is the OPPOSITE of what the part 1 solution does.
-- For example, we might have Bags["shiny gold"]["hearing aid beige"] == 3,
--  meaning that a shiny gold bag may contain 3 hearing aid beige bags.
Bags = {}

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
    -- Note that this means that bag colors that cannot contain other bags
    --  do not appear in our Bags table.
    return
  end
  -- This is the general case: the contents string contains at least one
  --  bag that may be enclosed in a `bagname` bag. Identify, non-greedily
  --  (hence `(.-)`) the first bag's `number` and `color`, storing the
  --  remainder for later processing.
  local number, color, remainder = string.match(contents, "(%d) (.-) bags?[,.]%s?(.*)")
  
  if Bags[bagname] == nil then
    Bags[bagname] = {}
  end
  
  Bags[bagname][color] = number
  
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

-- Returns how many total bags are held in an `enclosingbag` color bag.
function Howmanybagsheld(enclosingbag)
  local count = 0

  -- Base case: If `enclosingbag` doesn't hold anything, then the
  --  number of bags held is 1: just the `enclosingbag` itself.
  if not Bags[enclosingbag] then
    return 1
  end

  -- Otherwise, our bag does have some contents. The color and number
  --  of each enclosed bag is captured in this for loop:
  for heldbag, ct in pairs(Bags[enclosingbag]) do
    -- Increase our count by the product of `ct` (the quantity of 
    --  `heldbag`s in `enclosingbag` and a recursive call to this
    --  function, which tells us how many bags are inside `heldbag`.)
    count = count + ct * Howmanybagsheld(heldbag)
  end
  return 1 + count
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
Recordbags(arg[1])

-- We subtract 1 here, because we don't want to count the gold bag.
print(Howmanybagsheld("shiny gold")-1)
