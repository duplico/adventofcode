import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Parameters;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.concurrent.Callable;

@Command(name = "advent4a", mixinStandardHelpOptions = true, description = "Solve the 2020 Advent of Code day 4 passport part 1.")
class Advent4A implements Callable<Integer> {

    @Parameters(index = "0", description = "The input flie.", defaultValue = "sample_input.txt")
    private File inputFile;

    @Override
    public Integer call() throws Exception { // your business logic goes here...
        printValidRecordCount(inputFile);
        return 0;
    }

    private void printValidRecordCount(File inputFile) throws FileNotFoundException{
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

    private static boolean doAllFieldsValidate(String recordString) {
        // TODO: I suspect we may ultimately want to do something like this:
        // String[] entries = record.split("\\s");

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

        return true;
    }

    public static void main(String... args) {
        int exitCode = new CommandLine(new Advent4A()).execute(args);
        System.exit(exitCode);
    }
}
