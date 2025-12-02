use std::env;
use std::fs;

fn part1(filename: &str, verbose: bool) {
    let _input = fs::read_to_string(filename).unwrap();
    
    if verbose {
        println!("Running part 1 with verbose output...");
    }
    
    // TODO: Implement part 1
    println!("Part 1: {}", 0);
}

fn part2(filename: &str, verbose: bool) {
    let _input = fs::read_to_string(filename).unwrap();
    
    if verbose {
        println!("Running part 2 with verbose output...");
    }
    
    // TODO: Implement part 2
    println!("Part 2: {}", 0);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 3 {
        eprintln!("Usage: {} <part> <filename> [-v]", args[0]);
        std::process::exit(1);
    }
    
    let part = &args[1];
    let filename = &args[2];
    let verbose = args.get(3).map(|s| s == "-v").unwrap_or(false);
    
    match part.as_str() {
        "1" => part1(filename, verbose),
        "2" => part2(filename, verbose),
        _ => eprintln!("Unknown part: {}. Use 1 or 2.", part),
    }
}
