<template>
  <div class="home">
    <div>
    <div class="inp-cont">
      <input class="team-input" @click="toggleDropdown" v-model="filterText" placeholder="Type to filter teams" />
      <button @click="getRequest">Submit</button>
    </div>
    
    <div class="custom-dropdown">
      <!-- <div class="selected-option" @click="toggleDropdown">{{ selectedTeam }}</div> -->
      <!-- <div v-if="isDropdownOpen" :class="{ 'options': true, 'visible': isDropdownOpen }"> -->
      <div :class="{ 'options': true, 'visible': isDropdownOpen  }"> 
        <div v-for="team in filteredTeams" @click="selectTeam(team)">
          {{ team }}
        </div>
        
      </div>
      
    </div>
    <p>Filter Text: {{ filterText }}</p>
  </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue"
import axios from "axios"

export default {
  name: 'HomeView',
  components: {
    Header
  },
  data () {
    return {
      filterText: "",
      isDropdownOpen: false,
      selectedTeam: "",
      teams : [
      "Atlanta Hawks",
      "Boston Celtics",
      "Brooklyn Nets",
      "Charlotte Hornets",
      "Chicago Bulls",
      "Cleveland Cavaliers",
      "Dallas Mavericks",
      "Denver Nuggets",
      "Detroit Pistons",
      "Golden State Warriors",
      "Houston Rockets",
      "Indiana Pacers",
      "Los Angeles Clippers",
      "Los Angeles Lakers",
      "Memphis Grizzlies",
      "Miami Heat",
      "Milwaukee Bucks",
      "Minnesota Timberwolves",
      "New Orleans Pelicans",
      "New York Knicks",
      "Oklahoma City Thunder",
      "Orlando Magic",
      "Philadelphia 76ers",
      "Phoenix Suns",
      "Portland Trail Blazers",
      "Sacramento Kings",
      "San Antonio Spurs",
      "Toronto Raptors",
      "Utah Jazz", 
      "Washington Wizards"],
    }
    
  },
  computed: {
    filteredTeams() {
      return this.teams.filter(team =>
        team.toLowerCase().includes(this.filterText.toLowerCase())
      );
    },
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    selectTeam(team) {
      this.selectedTeam = team;
      this.isDropdownOpen = false;
      this.filterText = team
    },

    async getRequest () {
      const res = await fetch("http://127.0.0.1:5000", {
          sus: "sus"
        });

        const data = await res.json()
        console.log(data)
    }
  },
}
</script>


<style scoped>
  select {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }

  .inp-cont {
    display: flex;
    justify-content: center;
    align-items: center;
  }

.team-input {
  display: flex;
  justify-content: center;
  align-items: center;
  -webkit-appearance: none;
  outline: none;
  border: none;
  /* width: 200px; */
  border-radius: 4em;
  transition: border 1s ease-in-out;
  font-size: 1em;
  padding: 0.75em;
}



.custom-dropdown {
  display: flex;
  justify-content: center;
  align-items: center;
}

.selected-option {
  cursor: pointer;
  padding: 10px;
  /* border: 1px solid #3498db; */
  border-radius: 4px;
  background-color: #3498db;
  color: #fff;
}

.options {
  /* flex: auto; */
  /* position: center; */
  top: 100%;
  left: 0;
  width: 15%;
  background-color: #fff;
  border: 1px solid #3498db;
  border-top: none;
  border-radius: 0 0 4px 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1;

  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-in-out;
}

.options.visible {
  /* Set max-height to a sufficiently large value to show all options */
  max-height: 80em;
}

.options div {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.options div:hover {
  background-color: #f0f0f0;
}

</style>