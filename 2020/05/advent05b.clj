(ns advent05b
  (:require [clojure.string :as str] clojure.java.io))

(defn row-col-number [min max spec]
  (if (= min max)
    min
    (let [mid (quot (+ max min) 2)]
      (if (or (str/starts-with? spec "F") (str/starts-with? spec "L"))
        (recur min mid (subs spec 1)) ; Front or Left
        (recur (+ mid 1) max (subs spec 1))))))

(defn seat-id [spec]
    (+ (* 8 (row-col-number 0 127 (subs spec 0 7)))
       (row-col-number 0 7 (subs spec 7))))

(defn all-seat-ids [input-file-path]
  (with-open [input (clojure.java.io/reader input-file-path)]
    (sort (seq (map seat-id (line-seq input))))))

(defn missing-seat-id [seats]
  (if (= (inc (first seats)) (second seats))
    (recur (next seats))
    (inc (first seats))))

(println (missing-seat-id (all-seat-ids (first *command-line-args*))))
