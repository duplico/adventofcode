use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    // Yet again, we have something similar to Conway's Game of Life.
    // Active, 2 or 3 active neighbors: Active
    //                            else: Inactive
    // Inactive, 3 active neighbors:    Active
    //                            else: Inactive

    // Read the file and determine the dimensions
    
    const ROUNDS: usize = 6;

    let mut x_sz: usize = 0;
    let mut y_sz: usize = 0;
    let mut z_sz: usize = 1;
    let mut w_sz: usize = 1;
    let mut input_lines = vec![];
    
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(line) = line {
                if x_sz == 0 {
                    x_sz = line.len();
                }
                y_sz+=1;
                input_lines.push(line);
            }
        }
    }

    // Create a 3D array with 6 units of padding in all directions.
    x_sz += ROUNDS*2;
    y_sz += ROUNDS*2;
    z_sz += ROUNDS*2;
    w_sz += ROUNDS*2;

    let mut cube = vec![vec![vec![vec![0; x_sz]; y_sz]; z_sz]; w_sz];

    for y in 0..input_lines.len() {
        let chars: Vec<char> = input_lines[y].chars().collect();
        for x in 0..chars.len() {
            cube[ROUNDS][ROUNDS][ROUNDS+y][ROUNDS+x] = if chars[x] == '#' { 1 } else { 0 }
        }
    }

    let mut active_curr = 0;

    for _round in 0..ROUNDS {
        active_curr = 0;
        // Propagate each `1` to its neighbors:
        let mut cube_neighbors = vec![vec![vec![vec![0; x_sz]; y_sz]; z_sz]; w_sz];
        for x in 0..x_sz {
            for y in 0..y_sz {
                for z in 0..z_sz {
                    for w in 0..w_sz {
                        if cube[w][z][y][x] == 1 {
                            active_curr += 1;
                            for x_offset in (x-1)..(x+2) {
                                for y_offset in (y-1)..(y+2) {
                                    for z_offset in (z-1)..(z+2) {
                                        for w_offset in (w-1)..(w+2) {
                                            if x_offset == x && y_offset == y && z_offset == z && w_offset == w {
                                                continue;
                                            }
                                            cube_neighbors[w_offset][z_offset][y_offset][x_offset] += 1;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        // Now apply the rules:
        for x in 0..x_sz {
            for y in 0..y_sz {
                for z in 0..z_sz {
                    for w in 0..w_sz {
                        if cube[w][z][y][x] == 1 {
                            // Spot currently active. 
                            // 2-3 active neighbors -> active
                            // else -> inactive
                            if cube_neighbors[w][z][y][x] < 2 || cube_neighbors[w][z][y][x] > 3 {
                                cube[w][z][y][x] = 0;
                                active_curr -= 1;
                            }
                        } else {
                            // Spot currently inactive. It gets activated if it has
                            //  exactly 3 neighbors.
                            if cube_neighbors[w][z][y][x] == 3 {
                                cube[w][z][y][x] = 1;
                                active_curr += 1;
                            }
                        }
                    }
                }
            }
        }
    }

    println!("{}", active_curr);
}
