(ns advent
  (:require [clojure.string :as str])
  (:gen-class))

(def ^:dynamic *verbose* false)

(defn read-lines
  "Read all lines from a file, stripping whitespace."
  [filename]
  (-> filename slurp str/trim (str/split-lines)))

(defn valid-id-part2?
  "Check if the given ID is valid according to puzzle rules."
  (^Boolean [^long id] (valid-id-part2? id 1))
  (^Boolean [^long id ^long sublen]
   ;; cast ID to string
   ;; if sublen > (len id) return false; else:
   ;; split into substrings of length sublen
   ;; check if *all* substrings are equal
   ;; if all equal, return false; else return (valid-id? id (+ sublen 1))
   (let [id-str (str id) id-len (count id-str)] ; cast to string and get length
     (when *verbose*
       (println (format "  Checking id=%s with sublen=%d (id-len=%d)" id-str sublen id-len)))
     (if (> sublen (/ id-len 2)) ; base case: sublen exceeds id length
       (do
         (when *verbose*
           (println (format "  -> sublen > id-len, returning true (valid)")))
         true)
       (let [divisible? (== 0 (mod id-len sublen))
             substrings (when divisible?
                          (map #(subs id-str % (+ % sublen)) (range 0 id-len sublen)))
             all-equal? (when divisible? (apply = substrings))]
         (when *verbose*
           (println (format "    divisible? %s" divisible?))
           (when divisible?
             (println (format "    substrings: %s" (pr-str (vec substrings))))
             (println (format "    all-equal? %s" all-equal?))))
         (if (and divisible? all-equal?)
           (do
             (when *verbose*
               (println (format "  -> All substrings equal, returning false (invalid)")))
             false)
           (recur id (+ sublen 1))))))))

(defn valid-id-part1?
  "Check if the given ID is valid according to part 1's *actual* rules."
  (^Boolean [^long id]
   (let [id-str (str id)
         id-len (count id-str)
         half-len (/ id-len 2)
         first-half (subs id-str 0 half-len)
         second-half (subs id-str half-len)]
     (when *verbose*
       (println (format "  Checking id=%s: first-half=%s, second-half=%s"
                        id-str first-half second-half)))
     (cond
       (odd? id-len)
       (do
         (when *verbose*
           (println (format "  -> Odd length, returning true (invalid)")))
         true)

       (= first-half second-half)
       (do
         (when *verbose*
           (println (format "  -> Halves equal, returning false (invalid)")))
         false)

       :else
       (do
         (when *verbose*
           (println (format "  -> Halves not equal, returning true (valid)")))
         true)))))

(defn valid-id?
  "Check if the given ID is valid according to the specified part's rules."
  (^Boolean [^long id ^long part]
   (case part
     1 (valid-id-part1? id)
     2 (valid-id-part2? id)
     (do
       (when *verbose*
         (println (format "  Unknown part %d, exiting" part)))
       (throw (IllegalArgumentException. (format "Unknown part: %d" part)))))))

(defn add-id-if-invalid
  ^long [^long acc ^long id ^long part]
  (if (valid-id? id part)
    (do
      (when *verbose*
        (println (format "ID %d is valid, skipping." id)))
      acc)
    (do
      (when *verbose*
        (println (format "ID %d is invalid, adding to sum." id)))
      (+ acc id))))

(defn sum-invalid-ids
  "Sum all invalid IDs from the list."
  (^long [ids ^long part]
   (reduce (fn [acc id] (add-id-if-invalid acc id part))
           0
           ids))
  (^long [^long id-start ^long id-end ^long part]
   (sum-invalid-ids (range id-start (inc id-end)) part)))

(defn sum-invalid-id-string-range
  "Sum all invalid IDs from a string of <start>-<end>."
  ^long
  [^String id-range-str ^long part]
  (let [[start-str end-str] (str/split id-range-str #"-")
        id-start (Long/parseLong start-str)
        id-end (Long/parseLong end-str)]
    (when *verbose*
      (println (format "Processing ID range: %d-%d" id-start id-end)))
    (sum-invalid-ids id-start id-end part)))

(defn part1
  "Solve part 1 of the puzzle."
  [filename]
  (let [id-ranges (-> filename slurp str/trim (str/split #","))
        result (reduce + (map #(sum-invalid-id-string-range % 1) id-ranges))]
    (when *verbose*
      (println (format "Read %d id ranges from %s" (count id-ranges) filename)))
    (println (format "Part 1: %d" result))
    result))

(defn part2
  "Solve part 2 of the puzzle."
  [filename]
  (let [id-ranges (-> filename slurp str/trim (str/split #","))
        result (reduce + (map #(sum-invalid-id-string-range % 2) id-ranges))]
    (when *verbose*
      (println (format "Read %d id ranges from %s" (count id-ranges) filename)))
    (println (format "Part 2: %d" result))
    result))

(defn -main
  "Main entry point."
  [& args]
  (let [[part filename & opts] args
        verbose? (some #{"-v"} opts)]
    (when (or (nil? part) (nil? filename))
      (println "Usage: clj -M:run <part> <filename> [-v]")
      (System/exit 1))

    (binding [*verbose* verbose?]
      (case part
        "1" (part1 filename)
        "2" (part2 filename)
        (do
          (println (format "Unknown part: %s. Use 1 or 2." part))
          (System/exit 1))))))
