import java.io.File

fun main() {
     var totalCount : Int = 0;
     val groupQuestions = mutableSetOf<Char>();

     File("input.txt").forEachLine { 
          if (it == "") {
               // We've hit a blank line. Time to accumulate the current count,
               //  and clear our set.
               totalCount += groupQuestions.size
               groupQuestions.clear()
          }
          for (c in it) {
               groupQuestions.add(c)
          }
     }

     // Finally, add the last group's questions to the total.
     totalCount += groupQuestions.size

     println(totalCount)
}
