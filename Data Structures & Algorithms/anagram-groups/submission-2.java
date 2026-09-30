class Solution {

    private String getAnagram(String s) {
        return IntStream.range(0, s.length())
            .mapToObj(i -> s.charAt(i))
            .sorted()
            .map(String::valueOf)
            .collect(Collectors.joining());
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> anagrams = new HashMap<>();

        for (String s: strs) {
            String anagram = getAnagram(s);

            if (anagrams.containsKey(anagram)) {
                anagrams.get(anagram).add(s);
            }
            else {
                ArrayList<String> l = new ArrayList<String>();
                l.add(s);
                anagrams.put(anagram, l);
            }
        }

        List<List<String>> result = new ArrayList<>(anagrams.values());
        return result;
    }
}
