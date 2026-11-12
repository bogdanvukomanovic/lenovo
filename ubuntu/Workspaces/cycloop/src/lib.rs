use std::ops::Deref;
use geo::{CoordNum, LineString};

struct Lap<T: CoordNum>(pub LineString<T>);

pub struct Cycle<T: CoordNum> {
    estimated_cycle: Lap<T>,
    laps: Vec<Lap<T>>
    

impl<T: CoordNum> Lap<T> {
    fn is_lap(&self) -> bool {
        // TODO: Define proximity function for GPS coordinates
        self.0.is_closed()
    }
}

impl<T: CoordNum> Deref for Lap<T> {
    type Target = LineString<T>;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

impl<T: CoordNum> Cycloop<T> {
    pub fn detect_cycles(&self) -> Option<Vec<Cycle<T>>> {
        // TODO: Implement actual algorithm
        let dummy_cycle = Cycle {
            estimated_cycle: Lap(self.points.clone()),
            laps: vec![] 
        };
        let cycles: Vec<Cycle<T>> = vec![dummy_cycle];
        if self.points.is_closed() {
            Some(cycles)
        } else {
            None
        }
    }
}
