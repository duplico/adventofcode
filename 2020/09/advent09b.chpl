prototype module Advent09a {
     use IO;
     use DistributedDeque;

     config const invalid_value : int = 127;
     config const input_path : string = "sample_input.txt";

     var input_file : file;

     proc xmas_weakness() : int {
          var deque = new DistDeque(int);
          
          input_file = open(input_path, iomode.r);
          
          var file_reader = input_file.reader();
          var total = 0;
          var next_value : int;
          var has_elem : bool;

          while (total != invalid_value) {
               if total < invalid_value {
                    // if too low, add a new high one and add it to total
                    file_reader.read(next_value);
                    total += next_value;
                    deque.enqueue(next_value);
               } else {
                    // if too high, remove the low one and subtract it from total.
                    (has_elem, next_value) = deque.dequeue();
                    if !has_elem {
                         // Error!
                         exit(1);
                    }
                    total -= next_value;
               }
          }

          input_file.close();

          var low : int = invalid_value;
          var high : int = 0;

          for next_value in deque.these(Ordering.FIFO) {
               if next_value < low then
                    low = next_value;
               if next_value > high then
                    high = next_value;
          }

          return low + high;
     }

     proc main() {
          input_file = open(input_path, iomode.r);
          writeln("XMAS weakness found: ", xmas_weakness());
          input_file.close();
     }
}
