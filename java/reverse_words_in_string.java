class reverse_words_in_string {
    public String reverseWords(String s) {
        if(s.equals(null) || s.equals("")) {
            return s;
        }

        String result = "";
        int i = 0;

        while(i < s.length()) {
            while(i < s.length() && s.charAt(i) == ' ') {
                i++;
            }

            String word = "";

            // "  Hello " -> "Hello"
            while(i < s.length() && s.charAt(i) != ' ') {
                word += s.charAt(i);
                i++;
            }

            if(!word.equals("")) {
                result = word + " " + result;
            }
        }

        if(result.isEmpty()) return "";

        return result.substring(0, result.length() - 1);
    }
}