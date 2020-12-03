Param ($InputFile="input.txt")

$invalid_count = 0
$total_count = 0

# NB: Memory performance of Get-Content is potentially bad;
#     it will read the entire file into memory.
# Foreach-Object, on the other hand, processes it streamwise.

Get-Content $InputFile | ForEach-Object {
     if ($_ -match '(?<Min>\d+)\-(?<Max>\d+) (?<Letter>.): (?<Password>.+)') {
          $char_count = ($Matches.Password.ToCharArray() -eq $Matches.Letter).count
          if ($char_count -gt $Matches.Max -or $char_count -lt $Matches.Min) {
               $invalid_count++
          }
          $total_count++
     } else {
          Write-Error "Detected malformed input: $_"
     }
}

Write-Output "Invalid passwords: $invalid_count of $total_count"
