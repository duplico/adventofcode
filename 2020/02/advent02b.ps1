Param ($InputFile="input.txt")

$valid_count = 0
$total_count = 0

# NB: Memory performance of Get-Content is potentially bad;
#     it will read the entire file into memory.
# Foreach-Object, on the other hand, processes it streamwise.

Get-Content $InputFile | ForEach-Object {
     if ($_ -match '(?<First>\d+)\-(?<Second>\d+) (?<Letter>.): (?<Password>.+)') {
          $chars = $Matches.Password.ToCharArray()
          if ($chars[$Matches.First - 1] -eq $Matches.Letter -xor $chars[$Matches.Second - 1] -eq $Matches.Letter) {
               $valid_count++
          }
          $total_count++
     } else {
          Write-Error "Detected malformed input: $_"
     }
}

Write-Output "Valid passwords: $valid_count of $total_count"
