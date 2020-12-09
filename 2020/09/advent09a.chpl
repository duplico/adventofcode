prototype module Advent09a {
     use IO;

     config const window_size : int = 5;
     config const input_path : string = "sample_input.txt";

     var input_file : file;
     var window: [0..window_size-1] int;

     // TODO: Parallelize this!
     proc entry_valid(entry : int) : bool {
          for i in 0..window_size-1 {
               for j in i+1..window_size-1 {
                    if window[i]+window[j] == entry then return true;
               }
          }
          return false;
     }

     proc find_invalid_entry() {
          input_file = open(input_path, iomode.r);
          
          var file_reader = input_file.reader();
          var window_pos = 0;
          
          // Let's run through the first window_size entries first,
          //  because these make up our initial vector.
          while (window_pos < window_size) {
               if !file_reader.read(window[window_pos]) {
                    // This shouldn't happen with properly formed input files,
                    //  but we'll check anyway.
                    writeln("Read error. Ran out of values too soon.");
                    exit(1);
               }
               window_pos+=1;
          }

          // Now, we have our initial vector loaded. Reset window position to
          //  start by overwriting the oldest data in the sliding window.
          window_pos = 0;
          var next_value : int;

          // Now, let's scan the rest of the file.
          while (file_reader.read(next_value)) {
               // If the entry is invalid...
               if !entry_valid(next_value) {
                    // We're done. Print it and break, so we can clean up.
                    writeln("Invalid value ", next_value);
                    break;
               }

               // Otherwise, this is a valid entry, and it needs to be added
               //  to our sliding window. Put it in the oldest slot, and then
               //  increment our window position, wrapping it if needed.
               window[window_pos] = next_value;
               window_pos = (window_pos + 1) % window_size;
          }

          input_file.close();
     }

     proc main() {
          find_invalid_entry();
     }
}
