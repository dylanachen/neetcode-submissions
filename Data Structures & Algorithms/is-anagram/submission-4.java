class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), 1 + countS.getOrDefault(s.charAt(i), 0));
            countT.put(t.charAt(i), 1 + countT.getOrDefault(t.charAt(i), 0));
        }

        return countS.equals(countT);
    }
}
