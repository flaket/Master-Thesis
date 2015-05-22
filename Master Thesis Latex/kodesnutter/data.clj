(def initial-state
    {:rooms
        {
        ..
        :kitchen
            {:stove {:active? false, :temp nil}
             :oven  {:active? false, :temp nil}
             :dish-washer {:active? false, :time-remaining 45}
             :fridge    ["Eggs" "Bacon" ..]
             :lights-off? false}
        ..
        }
    ..
    :view    :home
    ..
    })