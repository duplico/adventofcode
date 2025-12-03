(ns advent
  (:require [clojure.string :as str])
  (:gen-class))

(def ^:dynamic *verbose* false)

(defn read-lines
  "Read all lines from a file, stripping whitespace."
  [filename]
  (-> filename slurp str/trim (str/split-lines)))

(defn shift-or-keep
  "Given a vector of digits, recursively build the maximum number by replacing the current
   number with either:
   - keeping it as is
   - shifting in the next digit at the tens place (with the current tens place moving to ones)
   - swapping in the next digit at the tens place (keeping the ones place)

   Returns the maximum number that can be formed."
  ^Long
  ([digits ^long num]
   (let [tens (quot num 10) ; current tens place of best candidate so far
         ones (mod num 10)  ; current ones place of best candidate so far
         new-digit (peek digits) ; next digit to consider (rightmost in remaining vector)
         candidate1 num ; option to keep current number as is
         candidate2 (+ (* new-digit 10) tens) ; option to shift in new digit at tens place
         candidate3 (+ (* new-digit 10) ones) ; option to swap in new digit at tens place
         new-number (long (max candidate1 candidate2 candidate3))
         new-digits (pop digits)]
     (when *verbose*
       (println (format "  digits=%s num=%d -> candidates: %d, %d, %d -> best=%d"
                        digits num candidate1 candidate2 candidate3 new-number)))
     (cond
       (empty? new-digits)
       (do
         (when *verbose*
           (println (format "  Done: returning %d" new-number)))
         new-number)
       :else (recur new-digits new-number))))
  ([^String line]
   (let [digits (vec (map #(Character/digit % 10) line))]
     (shift-or-keep (pop digits) (peek digits)))))


(defn part1
  "Solve part 1 of the puzzle."
  [filename]
  (let [lines (read-lines filename)]
    (when *verbose*
      (println (format "Read %d lines from %s" (count lines) filename)))

    ;; Sum shift-or-keep for all lines
    (let [result (reduce + (map shift-or-keep lines))]
      (println (format "Part 1: %d" result)))))

(defn part2
  "Solve part 2 of the puzzle."
  [filename]
  (let [lines (read-lines filename)]
    (when *verbose*
      (println (format "Read %d lines from %s" (count lines) filename)))

    ;; TODO: Implement solution
    (let [result 0]
      (println (format "Part 2: %d" result)))))

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
