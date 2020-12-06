import java.io.File

fun main() {
     var groupAnswers = mutableListOf<Set<Char>>()
     var allGroupAnswers = mutableListOf<List<Set<Char>>>()

     File("input.txt").forEachLine { 
          if (it == "") {
               // We've hit a blank line. Time to accumulate the current count,
               //  and clear our set.
               allGroupAnswers.add(groupAnswers)
               groupAnswers = mutableListOf<Set<Char>>()
          } else {
               groupAnswers.add(it.toSet())
          }
     }

     allGroupAnswers.add(groupAnswers)

     var answerCount = allGroupAnswers.map({group -> group.reduce({ a, b -> a union b}).size}).reduce({a, b -> a + b})

     println(answerCount)
}
