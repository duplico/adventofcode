import scala.io.Source
import scala.collection.mutable.ArrayBuffer

class Bus(val interval : Int, var departure : Long, val index : Int) {
     var fromLast : Int = index - Bus.lastBusIndex
     Bus.lastBusIndex = if (index > Bus.lastBusIndex) index else Bus.lastBusIndex
     var toNext : Int = 0

     // Overriding tostring method 
    override def toString() : String = { 
        "[..." + fromLast + " " + departure + "]"
    } 
}

object Bus {
     var lastBusIndex = 0
}

object Advent13b extends App {

     def syncBuses(bus0 : Bus, bus1 : Bus) : Boolean = {
          var targetVal : Long = 0L
          var workToDo = false
          var indexDiff = bus1.index - bus0.index
          while (bus0.departure + indexDiff != bus1.departure) {
               workToDo = true
               // println("Working on:")
               // println(" " + bus0 + " " + bus1)
               if (bus0.departure + indexDiff < bus1.departure) {
                    // bus0 is too low:
                    // bus0 needs to be advanced to be equal to or greater than
                    //  bus1.departure-indexDiff.
                    targetVal = bus1.departure-indexDiff
                    bus0.departure = (targetVal / bus0.interval) * bus0.interval
                    if (bus0.departure < targetVal) bus0.departure += bus0.interval
               } else {
                    // bus1 is too low:
                    // It needs to be at least bus0.departure+indexDiff
                    targetVal = bus0.departure+indexDiff
                    bus1.departure = (targetVal / bus1.interval) * bus1.interval
                    if (bus1.departure < targetVal) bus1.departure += bus1.interval
               }
               // println("Now:")
               // println(" " + bus0 + " " + bus1)
          }

          // if (workToDo) bus0.departure + indexDiff != bus1.departure else false
          workToDo
     }

     var filename : String = "sample_input.txt"
     if (args.length > 1) {
          println("Expected: Advent13a [input.txt]")
          sys.exit(1)
     } else if (args.length == 1) {
          filename = args(0)
     }
     
     val f = scala.io.Source.fromFile(filename)
     val lines = f.getLines()

     val arrivalTime : Int = lines.next().toInt

     var busIndex = 0
     var buses = new ArrayBuffer[Bus]()
     for (bus <- lines.next().split(",")) {
          if (bus != "x") {
               buses += new Bus(bus.toInt, bus.toInt, busIndex)
          }
          busIndex += 1
     }
     f.close()

     println("Initial input " + buses)

     var workToDo = true
     var iterations = 0L

     syncBuses(buses(0), buses(0))

     while (workToDo) {
          workToDo = false
          for (i <- Range(0, buses.length-1)) {
               // syncBuses returns true if there was work to do.
               if (syncBuses(buses(0), buses(i+1))) {
                    workToDo = true
               }
          }
          iterations+=1
          if (iterations == 1000000) {
               println("In progress:" + buses)
               iterations = 0
          }
     }

     // TODO:
     println(buses)
     // println(solved)
}
