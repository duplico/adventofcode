import scala.io.Source
import scala.collection.mutable.ArrayBuffer

class Bus(val interval : BigInt, val index : BigInt, val dontfix : Boolean = false) {
     var a = (interval-index) % interval // Remainder
     val n = interval
     if (a < 0) a = interval+a

     // Ugh, this is really ugly:
     if (dontfix) a = index

     // Overriding tostring method 
    override def toString() : String = { 
        "[..." + a + " " + interval + "]"
    } 
}

object Advent13b extends App {

     def euclidean_ex(a : BigInt, b : BigInt) : (BigInt, BigInt) = {
          // as + bt = gcd(a, b)
          // In this case, we'll know gcd=1
          var (old_r, r) = (a, b)
          var (old_s, s) = (BigInt(1L), BigInt(0L))
          var (old_t, t) = (BigInt(0L), BigInt(1L))
          var quotient : BigInt = 0L
          var tmp : BigInt = 0L

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
          
          println(s"Extended Euclidean of ${(a, b)} -> Bezout coeffs ${(old_s, old_t)} for gcf $old_r")

          // After that loop, the Bezout coefficients are old_s, old_t
          (old_s, old_t)
     }

     def crt_solve(buses : Bus*) : BigInt = {
          if (buses.size == 1) {
               // This is an error.
               println("Got unexpected buses length 1")
               sys.exit(1)
          } else if (buses.size == 2) {
               // TODO:
               // Base case: index = remainder = a; interval = divisor = n
               println(s"Base case: ${buses(0)} and ${buses(1)}")
               val (m0, m1) = euclidean_ex(buses(0).n, buses(1).n)
               var soln = (m1 * buses(0).a * buses(1).n + m0 * buses(1).a * buses(0).n) % (buses(0).n*buses(1).n)
               println(s"$m1 * ${buses(0).a} * ${buses(1).n} + $m0 * ${buses(1).a} * ${buses(0).n} = $soln (mod ${buses(0).n*buses(1).n})")
               if (soln < 0) {
                    println(s"Fixing to ${buses(0).n*buses(1).n + soln}")
                    buses(0).n*buses(1).n + soln
               }
               else
                    soln
          } else {
               // General case
               // val soln = crt_solve(buses(0), buses(1))
               crt_solve(List(new Bus(buses(0).n*buses(1).n, crt_solve(buses(0), buses(1)), true)) ++ buses.slice(2,buses.size): _*)
          }
     }

     var filename : String = "sample_input.txt"
     var cnt : Int = 0

     if (args.length > 2) {
          println("Expected: Advent13a [input.txt] [cnt]")
          sys.exit(1)
     } else if (args.length == 1) {
          filename = args(0)
     } else if (args.length == 2) {
          filename = args(0)
          cnt = args(1).toInt
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

     if (cnt == 0) cnt = buses.size

     println("Initial input " + buses)

     println(s"Soln: 0..$cnt " + crt_solve(buses.toList.slice(0,cnt): _*))

     // println(euclidean(7,13))
     // println(euclidean(0*13,1*7))

     // println(euclidean_ex(7,13))
     // println(euclidean_ex(0*13,1*7))
}
