use std::{collections::HashMap, fs};

fn main() {
    let content = fs::read_to_string("data.in").unwrap();

    println!("{}", first_part(&content));
    println!("{}", second_part(&content))
}

fn first_part(content: &str) -> i32 {
    let mut nm1: Vec<i32> = Vec::new();
    let mut nm2: Vec<i32> = Vec::new();

    for line in content.split("\n") {
        let numbs: Vec<&str> = line.split("   ").collect();

        if numbs.len() == 2 {
            nm1.push(numbs[0].parse().unwrap());
            nm2.push(numbs[1].parse().unwrap());
        }
    }

    nm1.sort();
    nm2.sort();

    let iter = nm1.iter().zip(nm2);
    let mut diff = 0;

    for pair in iter {
        diff += (pair.0 - pair.1).abs();
    }

    diff
}

fn second_part(content: &str) -> i32 {
    let mut score: i32 = 0;

    let mut nm1: Vec<i32> = Vec::new();
    let mut nm2: Vec<i32> = Vec::new();

    for line in content.split("\n") {
        let numbs: Vec<&str> = line.split("   ").collect();

        if numbs.len() == 2 {
            nm1.push(numbs[0].parse().unwrap());
            nm2.push(numbs[1].parse().unwrap());
        }
    }

    let hm1: HashMap<i32, i32> = compute_similarity(nm1);
    let hm2 = compute_similarity(nm2);

    for key in hm1.keys() {
        score += (key * hm2.get(key).unwrap_or(&0)) * hm1.get(key).unwrap_or(&0);
    }

    score
}

fn compute_similarity(nmbs: Vec<i32>) -> HashMap<i32, i32> {
    let mut hmap: HashMap<i32, i32> = HashMap::new();

    for nmb in nmbs {
        hmap.entry(nmb).and_modify(|count| *count += 1).or_insert(1);
    }

    hmap
}
