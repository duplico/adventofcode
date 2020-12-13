import scala.io.Source

object Advent13a extends App {
     var filename : String = "sample_input.txt"
     if (args.length > 1) {
          println("Expected: Advent13a [input.txt]")
          sys.exit(1)
     } else if (args.length == 1) {
          filename = args(0)
     }
     
     // TODO: Error handling/ "Using"
     val f = scala.io.Source.fromFile(filename)
     val lines = f.getLines()

     val arrivalTime : Int = lines.next().toInt

     val buses =
          for (bus <- lines.next().split(",") if bus != "x")
          yield bus.toInt
     
     f.close()

     // NB: This assumes that no bus departs at the exact same time
     //     as I arrive.
     var soonestBus : Int = 0
     var soonestWait : Int = 0

     for (bus <- buses) {
          val busWait = (arrivalTime / bus + 1) * bus - arrivalTime
          if (soonestBus==0 || busWait < soonestWait) {
               soonestBus = bus
               soonestWait = busWait
          }
     }

     println(soonestBus * soonestWait)
}
