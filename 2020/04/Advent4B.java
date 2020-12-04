import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Parameters;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.concurrent.Callable;

@Command(name = "advent4b", mixinStandardHelpOptions = true, 
         description = "Solve the 2020 Advent of Code day 4 passport part 1.")
class Advent4B implements Callable<Integer> {

    @Parameters(index = "0", description = "The input flie.", 
                defaultValue = "sample_input.txt")
    private File inputFile;

    @Override
    public Integer call() throws Exception {
        printValidRecordCount(inputFile);
        return 0;
    }

    private void printValidRecordCount(File inputFile) throws FileNotFoundException {
        Scanner scr = new Scanner(inputFile); 
        scr.useDelimiter("\n\n");
        
        int validRecordCount = 0;
        
        while (scr.hasNext()) {
            // Let's go ahead and replace any newlines with a space, to
            // sorta normalize this.
            String record = scr.next().replace('\n', ' ');
            if (doAllFieldsValidate(record)) {
                validRecordCount++;
            }
        }
        scr.close();

        System.out.println(validRecordCount);
    }

    private static boolean doesFieldValidate(String field, String data) {

        try {
            switch(field) {
            case "byr":
                if (Integer.parseInt(data) >= 1920 && Integer.parseInt(data) <= 2002)
                    return true;
                break;
            case "iyr":
                if (Integer.parseInt(data) >= 2010 && Integer.parseInt(data) <= 2020)
                    return true;
                break;
            case "eyr":
                if (Integer.parseInt(data) >= 2020 && Integer.parseInt(data) <= 2030)
                    return true;
                break;
            case "hgt":
                int val = Integer.parseInt(data.substring(0, data.length()-2));
                if (data.endsWith("cm")) {
                    if (val >= 150 && val <= 193)
                        return true;
                } else if (data.endsWith("in")) {
                    if (val >= 59 && val <= 76)
                        return true;
                }
                break;
            case "hcl":
                if (data.matches("#[\\da-f]{6}")) {
                    return true;
                }
                break;
            case "ecl":
                if (data.equals("amb") || data.equals("blu") || data.equals("brn") || data.equals("gry")
                 || data.equals("grn") || data.equals("hzl") || data.equals("oth"))
                    return true;
                break;
            case "pid":
                if (data.matches("\\d{9}"))
                    return true;
                break;
            case "cid":
                // Ignored.
                return true;
            default:
                return false;
            }
        } catch (Exception e) {
            // If something errored in parsing the data field, it's a fail.
            return false;
        }

        return false;
    }

    private static boolean doAllFieldsValidate(String recordString) {
        String[] requiredFields = {
            "byr:",
            "iyr:",
            "eyr:",
            "hgt:",
            "hcl:",
            "ecl:",
            "pid:",
            // "cid:", // OPTIONAL!
        };

        for (String requiredField : requiredFields) {
            if (!recordString.contains(requiredField)) {
                return false;
            }
        }

        // Now, separately, let's validate the fields.
        String[] fieldStrings = recordString.split("\\s");

        for (String fieldString : fieldStrings) {
            // TODO: Not sure whether the trim is needed.
            String[] parts = fieldString.trim().split(":");
            
            if (!doesFieldValidate(parts[0], parts[1])) {
                return false;
            }
        }

        return true;
    }

    public static void main(String... args) {
        int exitCode = new CommandLine(new Advent4B()).execute(args);
        System.exit(exitCode);
    }
}
