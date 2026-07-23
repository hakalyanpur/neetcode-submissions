class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordtoAnagramList = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            if (!wordtoAnagramList.containsKey(key)) {
                wordtoAnagramList.put(key, new ArrayList<>());
            }

            wordtoAnagramList.get(key).add(s);
        }

        return new ArrayList<>(wordtoAnagramList.values());
    }
}
