import java.io.File

fun groupAnswerCount(groupAnswers : List<Set<Char>>) : Int {
     return groupAnswers.reduce({a, b -> a intersect b}).size
}

fun main() {
     var groupAnswers = mutableListOf<Set<Char>>()
     var answerCount = 0

     File("input.txt").forEachLine { 
          if (it == "") {
               // We've hit a blank line. Time to accumulate the current count,
               //  and clear our set.
               answerCount += groupAnswerCount(groupAnswers)
               groupAnswers = mutableListOf<Set<Char>>()
          } else {
               groupAnswers.add(it.toSet())
          }
     }

     answerCount += groupAnswerCount(groupAnswers)

     println(answerCount)
}
