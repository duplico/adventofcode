(ns advent
  (:require [clojure.string :as str])
  (:gen-class))

(def ^:dynamic *verbose* false)

(defn read-lines
  "Read all lines from a file, stripping whitespace."
  [filename]
  (-> filename slurp str/trim (str/split-lines)))

(defn part1
  "Solve part 1 of the puzzle."
  [filename]
  (let [lines (read-lines filename)]
    (when *verbose*
      (println (format "Read %d lines from %s" (count lines) filename)))

    ;; TODO: Implement solution
    (let [result 0]
      (println (format "Part 1: %d" result)))))

(declare ways-to-bottom)

(defn ways-to-bottom*
  "Given a vector of row strings, and a current row and column,
   returns the number of possible paths to the bottom of the grid"
  ^Long [grid row col]
  (when *verbose*
    (println (format "  ways-to-bottom: row=%d col=%d char=%s" row col (get-in grid [row col]))))
  ;; Base case: if we're at the last row, there's only one way down
  (let [result (cond
                 (= row (dec (count grid))) 1
                 (= (get-in grid [row col]) \.) (ways-to-bottom grid (inc row) col)
                 (= (get-in grid [row col]) \^) (+ (ways-to-bottom grid row (inc col)) (ways-to-bottom grid row (dec col)))
                 :else 0)] ;; TODO: This should be an error case
    (when *verbose*
      (println (format "  ways-to-bottom: row=%d col=%d -> %d" row col result)))
    result))

(def ways-to-bottom (memoize ways-to-bottom*))

(defn part2
  "Solve part 2 of the puzzle."
  [filename]
  (let [lines (read-lines filename)]
    (when *verbose*
      (println (format "Read %d lines from %s" (count lines) filename)))

    (let [row 1
          col (-> lines first (.indexOf "S"))
          result (ways-to-bottom lines row col)]
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
