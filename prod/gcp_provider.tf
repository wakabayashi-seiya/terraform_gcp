provider "google" {
  project = "${var.project_name}"
  region = "${var.region}"
  credentials = "${file("${var.credential}")}"
}

resource "google_compute_instance" "apps_gcp_terraform" {
  name         = "${var.gce_name}"
  machine_type = "${var.machine_type}"
  zone         = "${var.zone}"
  tags = ["http-server", "https-server"]

  boot_disk {
	  initialize_params {
		size  = 30
		type  = "${var.boot_disk_type}"
		image = "${var.boot_disk_image}"
	  }
	}
	
  network_interface {
    network      = "default"
    access_config {
    nat_ip       = "${var.nat_ip}"
    network_tier = "${var.network_tier}"
            }
    }
}


resource "google_compute_firewall" "allow-http" {
  name    = "default-allow-http"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["80"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags = ["http-server"]
}

resource "google_compute_firewall" "allow-https" {
  name    = "default-allow-https"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["443"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags = ["https-server"]
}
