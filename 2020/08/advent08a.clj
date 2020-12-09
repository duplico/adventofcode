(require '[clojure.string :as str])

(defn val-at-loop [program-counter accumulator instructions]
    (if (nil? (nth instructions program-counter))
      accumulator
      (let [op (first (str/split (nth instructions program-counter) #" ")) 
            amt (Integer/parseInt (second (str/split (nth instructions program-counter) #" ")))]
        (recur
          (if (= op "jmp") (+ program-counter amt) (inc program-counter))
          (if (= op "acc") (+ accumulator amt) accumulator)
          (assoc instructions program-counter nil)))))

(println (val-at-loop 0 0 (str/split-lines (slurp "input.txt"))))
