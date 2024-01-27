<template>
  <div class="home">
    <form action="">
      <label for="teams">Select a Team</label>
      <select name="teams" id="dropdown" v-model="selectedTeam">
        <option v-for="team in teams"  :value="team">{{ team }}</option>
      </select>
    </form>    
    <p>{{ selectedTeam }}</p>
  </div>
</template>

<script>
import Header from "../components/Header.vue"

export default {
  name: 'HomeView',
  components: {
    Header
  },
  data () {
    return {
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
    
    
  }
}
</script>
