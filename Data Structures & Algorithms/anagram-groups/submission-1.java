class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> anagramMap = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            
            if (!anagramMap.containsKey(key)) {
                anagramMap.put(key, new ArrayList<>());
            }
            anagramMap.get(key).add(s);

        }
        return new ArrayList<>(anagramMap.values());
    }
}
