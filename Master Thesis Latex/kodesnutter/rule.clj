(defn stove-on []
  (when (and (:active? (:stove (:kitchen (:rooms @state))))
             (= :out (:current-location (:user @state))))
    (swap! state assoc :view :kitchen)))