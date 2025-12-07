(ns advent
  (:require [clojure.string :as str])
  (:gen-class))

(def ^:dynamic *verbose* false)

(defn read-lines
  "Read all lines from a file, stripping whitespace."
  [filename]
  (-> filename slurp str/trim (str/split-lines)))

(defn solve-column
  "Perform the computation specified by the final entry in the column on the rest of the entries."
  [col]
  (when *verbose*
    (println (format "Solving column: %s" col)))
  (let [operation (last col)
        numbers (map #(Integer/parseInt %) (butlast col))]
    (when *verbose*
      (println (format "Solving column with operation '%s' on numbers: %s" operation numbers)))
    (case operation
      "+" (reduce + numbers)
      "*" (reduce * numbers))))

(defn part1
  "Solve part 1 of the puzzle."
  [filename]
  (let [lines (map str/trim (read-lines filename))
        rows (map #(str/split % #"\s+") lines)
        cols (apply map vector rows)
        result (reduce + (map solve-column cols))]
    (when *verbose*
      (println (format "Read rows: %s" rows)))

    (println (format "Part 1: %d" result))))

(defn part2
  "Solve part 2 of the puzzle."
  [filename]
  (let [lines (read-lines filename)]
    (when *verbose*
      (println (format "Read %d lines from %s" (count lines) filename)))

    (println "Part 2 solution is not in clojure. Try python.")))

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
