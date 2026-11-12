use std::fs::File;
use std::io::{BufReader, Write};
use gpx;
use geo::ConvexHull;
use cycloop::{Cycloop, Cycle};

fn main() {
    println!("###################### CYCLOOP ######################");
    let file = File::open("data/data_0.gpx").unwrap();
    let reader = BufReader::new(file);
    let gpx: gpx::Gpx  = gpx::read(reader).unwrap();

    let mut points: geo::LineString = gpx.tracks[0].segments[0].points.iter().map(
        |waypoint: &gpx::Waypoint| waypoint.point().0
    ).collect::<geo::LineString<_>>();

    let convex_hull: geo::Polygon = points.convex_hull();
    let gps_output_filename = "data/gps-data.csv";
    let mut convex_hull_csv: File = File::create(gps_output_filename).unwrap();
    
    for point in convex_hull.exterior() {
        convex_hull_csv.write_fmt(format_args!("{},{}\n", point.x, point.y)).unwrap();
    }
    
    println!("Written raw GPS cooredinates to {}", gps_output_filename);
    println!("Looking for cycles...");

    points.close();     // <- Faking a cycle, comment/uncomment this line.

    let cycloop = Cycloop {points: points};
    if let Some(cycles) = cycloop.detect_cycles() {
        println!("Found {} cycles", cycles.len());
    } else {
        println!("No cycles found");
    }


}
