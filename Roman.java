

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Roman {

    private static final Map<Character, Integer> map;

    static {
        map = new HashMap<Character, Integer>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
    }

    public int romanToInt(String s) {
        if (s.length() == 1) {
            // Handle single-letter input
            char singleLetter = s.charAt(0);
            if (!map.containsKey(singleLetter)) {
                System.out.println("Invalid");
                return -1;  // or any other value indicating invalid input
            }
            return map.get(singleLetter);
        }

        int convertedNumber = 0;
        for (int i = 0; i < s.length(); i++) {
            int currentNumber = map.get(s.charAt(i));
            int next = i + 1 < s.length() ? map.get(s.charAt(i + 1)) : 0;
            if (currentNumber >= next) {
                convertedNumber += currentNumber;
            } else {
                convertedNumber -= currentNumber;
            }
        }
        return convertedNumber;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get user input for a Roman numeral
        System.out.print("Enter a Roman numeral: ");
        String userInput = scanner.nextLine();

        // Test the Roman class with user input
        Roman romanNumeral = new Roman();
        int result = romanNumeral.romanToInt(userInput);

        // Output the result
        if (result == -1) {
            System.out.println("Invalid input. Please enter a valid Roman numeral.");
        } else {
            System.out.println("Roman to Integer: " + result);
        }

    }
}
