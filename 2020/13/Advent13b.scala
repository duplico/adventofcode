import scala.io.Source
import scala.collection.mutable.ArrayBuffer

class Bus(val interval : Long, val index : Long) {

     // Overriding tostring method 
    override def toString() : String = { 
        "[..." + index + " " + interval + "]"
    } 
}

object Advent13b extends App {

     def euclidean_ex(a : Long, b : Long) : (Long, Long) = {
          // as + bt = gcd(a, b)
          // In this case, we'll know gcd=1
          var (old_r, r) = (a, b)
          var (old_s, s) = (1L, 0L)
          var (old_t, t) = (0L, 1L)
          var quotient : Long = 0L
          var tmp : Long = 0L

          while (r != 0) {
               quotient = old_r / r

               // (old_r, r) = (r, old_r - quotient * r)
               tmp = r
               r = old_r - quotient * r
               old_r = tmp

               // (old_s, s) = (s, old_s - quotient * s)
               tmp = s
               s = old_s - quotient * s
               old_s = tmp

               // (old_t, t) = (t, old_t - quotient * t)
               tmp = t
               t = old_t - quotient * t
               old_t = tmp
          }
          
          // After that loop, the Bezout coefficients are old_s, old_t
          (old_s, old_t)
     }

     def crt_solve(buses : Bus*) : Long = {
          if (buses.size == 1) {
               // This is an error.
               println("Got unexpected buses length 1")
               sys.exit(1)
          } else if (buses.size == 2) {
               // Base case: index = remainder = a; interval = divisor = n
               val (m0, m1) = euclidean_ex(buses(0).interval, buses(1).interval)
               val soln = (m1 * buses(0).index * buses(1).interval + m0 * buses(1).index * buses(0).interval) % (buses(0).interval * buses(1).interval)
               if (soln < 0)
                    buses(0).interval*buses(1).interval + soln
               else
                    soln
          } else {
               // General case
               // val soln = crt_solve(buses(0), buses(1))
               crt_solve(List(new Bus(buses(0).interval*buses(1).interval, crt_solve(buses.slice(0,2): _*))) ++ buses.slice(2,buses.size): _*)
          }
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

     lines.next() // Throw away the first line.

     var busIndex = 0
     var buses = new ArrayBuffer[Bus]()
     for (bus <- lines.next().split(",")) {
          if (bus != "x") {
               buses += new Bus(bus.toInt, busIndex)
          }
          busIndex += 1
     }

     f.close()



     println("Initial input " + buses)

     println("Soln: " + crt_solve(buses.toList: _*))
     // println(euclidean(7,13))
     // println(euclidean(0*13,1*7))

     // println(euclidean_ex(7,13))
     // println(euclidean_ex(0*13,1*7))
}
