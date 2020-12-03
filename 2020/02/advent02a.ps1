Param ($InputFile="input.txt")

$valid_count = 0
$total_count = 0

# NB: Memory performance of Get-Content is potentially bad;
#     it will read the entire file into memory.
# Foreach-Object, on the other hand, processes it streamwise.

Get-Content $InputFile | ForEach-Object {
     if ($_ -match '(?<Min>\d+)\-(?<Max>\d+) (?<Letter>.): (?<Password>.+)') {
          $char_count = ($Matches.Password.ToCharArray() -eq $Matches.Letter).count
          if ($char_count -le $Matches.Max -and $char_count -ge $Matches.Min) {
               $valid_count++
          }
          $total_count++
     } else {
          Write-Error "Detected malformed input: $_"
     }
}

Write-Output "Valid passwords: $valid_count of $total_count"
